
import requests

payload = {
  "query": """query ProductQuery(
    $ids: [Int!]
  ) {
    getProducts(
      ids: $ids
    ) {
      base_img_url          
      products {
        ...productFields
      children {
        ...productFields
          }
      }
    }
  }
  fragment productFields on Product {
    id
    desc
    pack_desc
    sp
    mrp
    w
    absolute_url
    images {
      s
    }
    discount {
      type
      value
    }
    brand {
      name
      slug
      url
    }
    additional_attr {
      food_type
      info {
        type
        image
        sub_type
        label
      }
    }
    combo_info {
      destination {
        display_name
        dest_type
        dest_slug
        url
      }
      total_saving_msg          
      items{
        id
        brand
        sp
        mrp
        is_express
        saving_msg
        link
        img_url
        qty
        wgt
        p_desc
      }
      total_sp
      total_mrp
      annotation_msg
    }
    sale {
      type
      display_message
      end_time
      maximum_redem_per_order
      maximum_redem_per_member
      show_counter
      message
      offers_msg
    }
    promo {
      type
      label
      id
      name
      saving
      savings_display
      desc
      url
      desc_label
    }
    discounted_price {
      display_name
      value
    }
    discounted_price_v2 {
      display_name
      value
    }
    rating_info  {
      avg_rating
      rating_count
      review_count
      sku_id
    }
  }""",


  "variables": {
    "ids": [],
    "visitorId": "0",
    "cityId": "1"
  }
}



s = requests.Session()

search_term = input("Input the item to be scraped?")
#FIRST PAGE
search_url = "https://www.bigbasket.com/custompage/getsearchdata/?slug="+search_term+"&type=deck"
search_resp = s.get(search_url)
search_results = search_resp.json()

data_url = "https://www.bigbasket.com/product-svc/v1/gql"

#GETTING DATA
res = search_results['json_data']['tab_info'][0]['product_info']['products']
for r in res:
    product_url = "https://www.bigbasket.com"+r['absolute_url']
    res = s.get(product_url)
    payload['variables']['ids'] = [r['sku']]
    req = s.post(data_url, json=payload)
    data = req.json()
    #INFO ABOUT PRICE AND STUFF
    products = data['data']['getProducts']['products']
    #print(products)
    print(products[0]['desc'])

    print("\n")

    print(products[0]['rating_info']['sku_id'])

    print("\n")

    #INFO ABOUT CATEGORY
    category_url = "https://www.bigbasket.com/api/v1/product/facet/"+str(r['sku'])+"/?_bb_client_type=web"
    category_req = s.get(category_url)
    print(category_req.json()['category']['top_category'][0]['url'])
    #print(category_req.json()['category']['sub_category']['809']['url'])

    print("\n"*10)



    






